import Mathlib

set_option autoImplicit false

theorem msl_rh_necessary_not_sufficient_081 (Obj : Type) (Crit RealRooted : Obj -> Prop) (w : Obj) (hw1 : Crit w) (hw2 : ¬ RealRooted w) : ¬ (∀ x : Obj, Crit x → RealRooted x) := by
  intro h
  exact hw2 (h w hw1)
