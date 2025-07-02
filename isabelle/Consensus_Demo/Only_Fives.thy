theory
  Only_Fives
imports
  Main
begin

inductive only_fives :: \<open>nat list \<Rightarrow> bool\<close> where
  \<open>only_fives []\<close> |
  \<open>\<lbrakk>only_fives xs\<rbrakk> \<Longrightarrow> only_fives (xs @ [5])\<close>

theorem only_fives_concat:
  assumes \<open>only_fives xs\<close> and \<open>only_fives ys\<close>
  shows \<open>only_fives (xs @ ys)\<close>
using assms proof (induction ys rule: List.rev_induct)
  case Nil
  then show \<open>only_fives (xs @ [])\<close>
    by simp
next
  case (snoc y ys)
  hence \<open>only_fives ys\<close>
    using only_fives.cases by auto
  hence \<open>only_fives (xs @ ys)\<close>
    by (simp add: snoc.IH snoc.prems(1))
  moreover have \<open>y = 5\<close>
    using only_fives.cases snoc.prems(2) by blast
  ultimately show \<open>only_fives (xs @ ys @ [y])\<close>
    using only_fives.intros(2) by fastforce
qed

end
