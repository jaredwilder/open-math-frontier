import Mathlib

set_option autoImplicit false

theorem msl_rh_consecutive_not_total_065 (a0 a1 a4 a5 : Real) (h0 : a0 = 1) (h1 : a1 = 0) (h4 : a4 = 0) (h5 : a5 = 1) : a1 * a4 - a5 * a0 = -1 := by
  subst h0; subst h1; subst h4; subst h5
  norm_num
