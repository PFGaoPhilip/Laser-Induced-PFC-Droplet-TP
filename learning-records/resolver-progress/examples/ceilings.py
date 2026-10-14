"""Conditional examples, not computed CFD objectives. Python standard library."""
import math

def ceiling(work_j, mass_kg):
    if work_j < 0 or mass_kg <= 0:
        raise ValueError('Require nonnegative work and positive mass')
    return math.sqrt(2 * work_j / mass_kg)

def contact(speed, z1, z2=None):
    if speed < 0 or z1 <= 0 or (z2 is not None and z2 <= 0):
        raise ValueError('Require positive impedances and nonnegative speed')
    return z1 * speed if z2 is None else z1 * z2 / (z1 + z2) * speed

def disk_window_constant(gauge_pa, radius_m, window_s):
    if radius_m <= 0 or window_s <= 0:
        raise ValueError('Positive disk and window required')
    integrated = gauge_pa * math.pi * radius_m**2 * window_s
    return integrated / (math.pi * radius_m**2 * window_s)

def main():
    rho, sound, radius, length, work = 1000., 1500., 3e-6, 50e-6, 5e-9
    mass = rho * math.pi * radius**2 * length
    speed = ceiling(work, mass)
    assert math.isclose(speed, 84.104417400672, rel_tol=1e-10)
    assert math.isclose(ceiling(4*work, mass), 2*speed)
    assert math.isclose(ceiling(work, 4*mass), speed/2)
    assert ceiling(0, mass) == 0
    z = rho * sound
    assert math.isclose(contact(speed,z,z), contact(speed,z)/2)
    for r in (2e-6,10e-6):
        for dt in (2e-9,20e-9):
            assert math.isclose(disk_window_constant(12345,r,dt),12345)
    print('Illustration mass kg:',mass,'jet m/s:',speed)
    print('Equal/rigid contact MPa:',contact(speed,z,z)/1e6,contact(speed,z)/1e6)
    for species, available in [('PFP',2.722572407203039e-9),('PFH',4.622122564638143e-9)]:
        print(species, 'conditional m/s:', [ceiling(available,m*1e-15) for m in (1,3,10,30,100)])
    print('PASS: analytical examples. NOT_RUN: native campaign, attained objectives.')

if __name__ == '__main__':
    main()
