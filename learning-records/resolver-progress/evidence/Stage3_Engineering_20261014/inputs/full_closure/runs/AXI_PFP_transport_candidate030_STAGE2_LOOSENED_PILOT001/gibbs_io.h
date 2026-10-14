/* Explicit little-endian CGIBBS1 table I/O. The in-memory ordering is
 * ix*nT+jT; the exchanged binary ordering is jT*nx+ix. No masked holes are
 * filled. Tables are immutable after loading. Original task-owned code. */
#ifndef CLOSURE_GIBBS_IO_H
#define CLOSURE_GIBBS_IO_H
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include "gibbs_potential.h"

typedef struct {
  ClosureGibbsTable table;
  double specific_gas_constant, critical_temperature, critical_density;
} ClosureGibbsFile;

static inline void closure_gibbs_free (ClosureGibbsFile * file) {
  free(file->table.x); free(file->table.temperature); free(file->table.nodes);
  memset(file,0,sizeof(*file));
}

static inline int closure_gibbs_load (const char * filename,
                                     ClosureGibbsFile * output) {
  memset(output,0,sizeof(*output));
  uint16_t endian = 1;
  if (*(uint8_t *)&endian != 1 || sizeof(double) != 8) return 1;
  FILE * input = fopen(filename,"rb");
  if (!input) return 2;
  char magic[8]; uint32_t n[2]; double properties[5];
  if (fread(magic,1,8,input) != 8 || memcmp(magic,"CGIBBS1\0",8) ||
      fread(n,sizeof(uint32_t),2,input) != 2 ||
      fread(properties,sizeof(double),5,input) != 5 ||
      n[0] < 2 || n[1] < 2 || (size_t)n[0]*n[1] > 100000000) {
    fclose(input); return 3;
  }
  ClosureGibbsTable * table = &output->table;
  table->nx = n[0]; table->nT = n[1];
  table->pressure_shift = properties[0]; table->pressure_scale = properties[1];
  output->specific_gas_constant = properties[2];
  output->critical_temperature = properties[3];
  table->shared_supercritical_temperature = properties[3];
  output->critical_density = properties[4];
  table->x = malloc(table->nx*sizeof(double));
  table->temperature = malloc(table->nT*sizeof(double));
  table->nodes = calloc(table->nx*table->nT,sizeof(ClosureGibbsNode));
  if (!table->x || !table->temperature || !table->nodes) {
    fclose(input); closure_gibbs_free(output); return 4;
  }
  if (fread(table->x,sizeof(double),table->nx,input) != table->nx ||
      fread(table->temperature,sizeof(double),table->nT,input) != table->nT) {
    fclose(input); closure_gibbs_free(output); return 5;
  }
  for (size_t jt = 0; jt < table->nT; jt++)
    for (size_t ix = 0; ix < table->nx; ix++) {
      double values[4];
      if (fread(values,sizeof(double),4,input) != 4) {
        fclose(input); closure_gibbs_free(output); return 6;
      }
      table->nodes[ix*table->nT+jt] = (ClosureGibbsNode)
        {values[0],values[1],values[2],values[3],0};
    }
  for (size_t jt = 0; jt < table->nT; jt++)
    for (size_t ix = 0; ix < table->nx; ix++) {
      int valid = fgetc(input);
      if (valid != 0 && valid != 1) {
        fclose(input); closure_gibbs_free(output); return 7;
      }
      table->nodes[ix*table->nT+jt].valid = valid;
    }
  if (fgetc(input) != EOF) {
    fclose(input); closure_gibbs_free(output); return 8;
  }
  for (size_t ix = 1; ix < table->nx; ix++)
    if (!(table->x[ix] > table->x[ix-1])) {
      fclose(input); closure_gibbs_free(output); return 9;
    }
  for (size_t jt = 1; jt < table->nT; jt++)
    if (!(table->temperature[jt] > table->temperature[jt-1])) {
      fclose(input); closure_gibbs_free(output); return 10;
    }
  fclose(input); return 0;
}
#endif
