#ifndef CLOSURE_EOS_DIAGNOSTIC_DUMP_H
#define CLOSURE_EOS_DIAGNOSTIC_DUMP_H
#include <stdio.h>
#include "eos_diagnostic_api.h"
static void closure_eos_diag_dump_header(FILE * file) {
  fputs("id,mode,leaf,index,stage,material_class,metric,calls,unsuccessful_calls,inclusive_CPU_seconds,invalid_context_requests,invalid_heat_node_requests,enabled,timing_enabled\n",file);
}
static void closure_eos_diag_dump(FILE * file,int id,int mode,int leaf,int index) {
  ClosureEOSDiagStats stats;closure_eos_diag_get_stats(&stats);int rows=0;
  for(int stage=-1;stage<CLOSURE_EOS_DIAG_STAGES;stage++) {
    int classes=stage<0?1:CLOSURE_EOS_DIAG_CLASSES;
    for(int k=0;k<classes;k++) {
      ClosureEOSDiagCell * cell=stage<0?&stats.unattributed:&stats.stage_class[stage][k];
      for(int metric=0;metric<CLOSURE_EOS_DIAG_METRICS;metric++)
        if(cell->calls[metric] || cell->unsuccessful_calls[metric] || cell->inclusive_CPU_seconds[metric]) {
          fprintf(file,"%d,%d,%d,%d,%d,%d,%d,%llu,%llu,%.17g,%llu,%llu,%d,%d\n",
            id,mode,leaf,index,stage,stage<0?-1:k,metric,cell->calls[metric],cell->unsuccessful_calls[metric],
            cell->inclusive_CPU_seconds[metric],stats.invalid_context_requests,stats.invalid_heat_node_requests,stats.enabled,stats.timing_enabled);
          rows++;
        }
    }
  }
  if(!rows)fprintf(file,"%d,%d,%d,%d,-1,-1,-1,0,0,0,%llu,%llu,%d,%d\n",id,mode,leaf,index,
    stats.invalid_context_requests,stats.invalid_heat_node_requests,stats.enabled,stats.timing_enabled);
  fflush(file);
}
#endif
