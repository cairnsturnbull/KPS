#define  PHYSICS                        RHD
#define  DIMENSIONS                     1
#define  GEOMETRY                       CARTESIAN
#define  BODY_FORCE                     NO
#define  COOLING                        NO
#define  RECONSTRUCTION                 LINEAR
#define  TIME_STEPPING                  RK2
#define  NTRACER                        0
#define  PARTICLES                      NO
#define  USER_DEF_PARAMETERS            0

/* -- physics dependent declarations -- */

#define  EOS                            IDEAL
#define  ENTROPY_SWITCH                 NO
#define  RADIATION                      NO

/* -- user-defined parameters (labels) -- */


/* [Beg] user-defined constants (do not change this line) */

#define  UNIT_LENGTH                    3.0e+10
#define  UNIT_DENSITY                   CONST_mp
#define  UNIT_VELOCITY                  CONST_c

/* [End] user-defined constants (do not change this line) */
