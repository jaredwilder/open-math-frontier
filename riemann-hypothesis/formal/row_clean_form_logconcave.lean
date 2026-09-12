import Mathlib

set_option autoImplicit false

theorem msl_rh_row_clean_form_logconcave_051 (P S k : Real) (hP : 0 < P) (hS : 0 < S) (hk : 0 < k) : (k + 1) * P <= k * (P + S) <-> P <= k * S := by
  constructor <;> intro h <;> nlinarith [h, hS, hP, hk]
