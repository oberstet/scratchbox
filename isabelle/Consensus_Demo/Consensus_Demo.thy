theory
  Consensus_Demo
imports
  Network
begin

datatype 'val msg
  = Propose 'val
  | Accept 'val

fun acceptor_step where
  \<open>acceptor_step state (Receive sender (Propose val)) =
     (case state of
        None   \<Rightarrow> (Some val, {Send sender (Accept val)}) |
        Some v \<Rightarrow> (Some v,   {Send sender (Accept v)}))\<close> |
  \<open>acceptor_step state _ = (state, {})\<close>

fun proposer_step where
  \<open>proposer_step None (Request val) = (None, {Send 0 (Propose val)})\<close> |
  \<open>proposer_step None (Receive _ (Accept val)) = (Some val, {})\<close> |
  \<open>proposer_step state _ = (state, {})\<close>

fun consensus_step where
  \<open>consensus_step proc =
     (if proc = 0 then acceptor_step else proposer_step)\<close>

(* Invariant 1: for any proposer p, if p's state is ``Some val'',
   then there exists a process that has sent a message
   ``Accept val'' to p. *)

definition inv1 where
  \<open>inv1 msgs states \<longleftrightarrow>
     (\<forall>proc val. proc \<noteq> 0 \<and> states proc = Some val \<longrightarrow>
                 (\<exists>sender. (sender, Send proc (Accept val)) \<in> msgs))\<close>

(* Invariant 2: if a message ``Accept val'' has been sent, then
   the acceptor is in the state ``Some val''. *)

definition inv2 where
  \<open>inv2 msgs states \<longleftrightarrow>
     (\<forall>sender recpt val. (sender, Send recpt (Accept val)) \<in> msgs \<longrightarrow>
                         states 0 = Some val)\<close>

lemma invariant_propose:
  assumes \<open>msgs' = msgs \<union> {(proc, Send 0 (Propose val))}\<close>
    and \<open>inv1 msgs states \<and> inv2 msgs states\<close>
  shows \<open>inv1 msgs' states \<and> inv2 msgs' states\<close>
proof -
  have \<open>\<forall>sender proc val.
      (sender, Send proc (Accept val)) \<in> msgs' \<longleftrightarrow>
      (sender, Send proc (Accept val)) \<in> msgs\<close>
    using assms(1) by blast
  then show ?thesis
    by (meson assms(2) inv1_def inv2_def)
qed

lemma invariant_decide:
  assumes \<open>states' = states (0 := Some val)\<close>
    and \<open>msgs' = msgs \<union> {(0, Send sender (Accept val))}\<close>
    and \<open>states 0 = None \<or> states 0 = Some val\<close>
    and \<open>inv1 msgs states \<and> inv2 msgs states\<close>
  shows \<open>inv1 msgs' states' \<and> inv2 msgs' states'\<close>
proof -
  {
    fix p v
    assume asm: \<open>p \<noteq> 0 \<and> states' p = Some v\<close>
    hence \<open>states p = Some v\<close>
      by (simp add: asm assms(1))
    hence \<open>\<exists>sender. (sender, Send p (Accept v)) \<in> msgs\<close>
      by (meson asm assms(4) inv1_def)
    hence \<open>\<exists>sender. (sender, Send p (Accept v)) \<in> msgs'\<close>
      using assms(2) by blast
  }
  moreover {
    fix p1 p2 v
    assume asm: \<open>(p1, Send p2 (Accept v)) \<in> msgs'\<close>
    have \<open>states' 0 = Some v\<close>
    proof (cases \<open>(p1, Send p2 (Accept v)) \<in> msgs\<close>)
      case True
      then show ?thesis
        by (metis assms(1) assms(3) assms(4) fun_upd_same inv2_def option.distinct(1))
    next
      case False
      then show ?thesis
        using asm assms(1) assms(2) by auto
    qed
  }
  ultimately show ?thesis
    by (simp add: inv1_def inv2_def)
qed

lemma invariant_learn:
  assumes \<open>states' = states (proc := Some val)\<close>
    and \<open>(sender, Send proc (Accept val)) \<in> msgs\<close>
    and \<open>inv1 msgs states \<and> inv2 msgs states\<close>
  shows \<open>inv1 msgs states' \<and> inv2 msgs states'\<close>
proof -
  {
    fix p v
    assume asm: \<open>p \<noteq> 0 \<and> states' p = Some v\<close>
    have \<open>\<exists>sender. (sender, Send p (Accept v)) \<in> msgs\<close>
    proof (cases \<open>p = proc\<close>)
      case True
      then show ?thesis
        using asm assms(1) assms(2) by auto
    next
      case False
      then show ?thesis
        by (metis asm assms(1) assms(3) fun_upd_apply inv1_def)
    qed
  }
  moreover {
    fix p1 p2 v
    assume \<open>(p1, Send p2 (Accept v)) \<in> msgs\<close>
    hence \<open>states' 0 = Some v\<close>
      by (metis assms fun_upd_apply inv2_def)
  }
  ultimately show ?thesis
    by (simp add: inv1_def inv2_def)
qed

lemma invariant_proposer:
  assumes \<open>proposer_step (states proc) event = (new_state, sent)\<close>
    and \<open>msgs' = msgs \<union> ((\<lambda>msg. (proc, msg)) ` sent)\<close>
    and \<open>states' = states (proc := new_state)\<close>
    and \<open>execute consensus_step (\<lambda>p. None) UNIV (events @ [(proc, event)]) msgs' states'\<close>
    and \<open>inv1 msgs states \<and> inv2 msgs states\<close>
  shows \<open>inv1 msgs' states' \<and> inv2 msgs' states'\<close>
proof (cases event)
  case (Receive sender msg)
  then show ?thesis
  proof (cases msg)
    case (Propose val)
    then show ?thesis
      using Receive assms by auto
  next
    case (Accept val) (* proposer receives Accept message: learn the decided value *)
    then show ?thesis
    proof (cases \<open>states proc\<close>)
      case None
      hence \<open>states' = states (proc := Some val) \<and> msgs' = msgs\<close>
        using Accept Receive assms(1) assms(2) assms(3) by auto
      then show ?thesis
        by (metis Accept Receive assms(4) assms(5) execute_receive invariant_learn)
    next
      case (Some v)
      then show ?thesis
        using assms by auto
    qed
  qed
next
  (* on a Request event, proposer sends a Propose message if its state
     is None, or ignores the event if already learnt a decision *)
  case (Request val)
  then show \<open>inv1 msgs' states' \<and> inv2 msgs' states'\<close>
  proof (cases \<open>states proc\<close>)
    case None
    hence \<open>states' = states \<and> msgs' = msgs \<union> {(proc, Send 0 (Propose val))}\<close>
      using Request assms(1) assms(2) assms(3) by auto
    then show ?thesis
      by (simp add: assms(5) invariant_propose)
  next
    case (Some v)
    then show ?thesis using assms by auto
  qed
next
  case Timeout
  then show \<open>inv1 msgs' states' \<and> inv2 msgs' states'\<close>
    using assms by auto
qed

lemma invariant_acceptor:
  assumes \<open>acceptor_step (states 0) event = (new_state, sent)\<close>
    and \<open>msgs' = msgs \<union> ((\<lambda>msg. (0, msg)) ` sent)\<close>
    and \<open>states' = states (0 := new_state)\<close>
    and \<open>execute consensus_step (\<lambda>p. None) UNIV (events @ [(0, event)]) msgs' states'\<close>
    and \<open>inv1 msgs states \<and> inv2 msgs states\<close>
  shows \<open>inv1 msgs' states' \<and> inv2 msgs' states'\<close>
proof (cases event)
  case (Receive sender msg)
  then show \<open>inv1 msgs' states' \<and> inv2 msgs' states'\<close>
  proof (cases msg)
    case (Propose val)
    then show ?thesis
    proof (cases \<open>states 0\<close>)
      case None (* not decided yet: decide now *)
      hence \<open>states' = states (0 := Some val) \<and>
             msgs' = msgs \<union> {(0, Send sender (Accept val))}\<close>
        using Receive Propose assms(1) assms(2) assms(3) by auto
        (* for some reason sledgehammer couldn't find the line above *)
      then show ?thesis
        by (simp add: None assms(5) invariant_decide)
    next
      case (Some val') (* already decided previously *)
      hence \<open>states' = states \<and>
             msgs' = msgs \<union> {(0, Send sender (Accept val'))}\<close>
        using Receive Propose assms(1) assms(2) assms(3) by auto
        (* for some reason sledgehammer couldn't find the line above *)
      then show ?thesis
        by (metis Some assms(3) assms(5) fun_upd_same invariant_decide)
    qed
  next
    case (Accept val)
    then show ?thesis
      using Receive assms by auto
  qed
next
  case (Request val)
  then show \<open>inv1 msgs' states' \<and> inv2 msgs' states'\<close>
    using assms by auto
next
  case Timeout
  then show \<open>inv1 msgs' states' \<and> inv2 msgs' states'\<close>
    using assms by auto
qed

lemma invariants:
  assumes \<open>execute consensus_step (\<lambda>x. None) UNIV events msgs' states'\<close>
  shows \<open>inv1 msgs' states' \<and> inv2 msgs' states'\<close>
using assms proof(induction events arbitrary: msgs' states' rule: List.rev_induct)
  case Nil
  from this show \<open>inv1 msgs' states' \<and> inv2 msgs' states'\<close>
    using execute_init inv1_def inv2_def by fastforce
next
  case (snoc x events)
  obtain proc event where \<open>x = (proc, event)\<close>
    by fastforce
  hence exec: \<open>execute consensus_step (\<lambda>p. None) UNIV
               (events @ [(proc, event)]) msgs' states'\<close>
    using snoc.prems by blast
  from this obtain msgs states sent new_state
    where step_rel1: \<open>execute consensus_step (\<lambda>x. None) UNIV events msgs states\<close>
      and step_rel2: \<open>consensus_step proc (states proc) event = (new_state, sent)\<close>
      and step_rel3: \<open>msgs' = msgs \<union> ((\<lambda>msg. (proc, msg)) ` sent)\<close>
      and step_rel4: \<open>states' = states (proc := new_state)\<close>
    by auto
  have inv_before: \<open>inv1 msgs states \<and> inv2 msgs states\<close>
    using snoc.IH step_rel1 by fastforce
  then show \<open>inv1 msgs' states' \<and> inv2 msgs' states'\<close>
  proof (cases \<open>proc = 0\<close>)
    case True
    then show ?thesis
      by (metis consensus_step.simps exec inv_before invariant_acceptor
          step_rel2 step_rel3 step_rel4)
  next
    case False
    then show ?thesis
      by (metis consensus_step.simps exec inv_before invariant_proposer
          step_rel2 step_rel3 step_rel4)
  qed
qed

theorem agreement:
  assumes \<open>execute consensus_step (\<lambda>x. None) UNIV events msgs states\<close>
    and \<open>states proc1 = Some val1\<close> and \<open>states proc2 = Some val2\<close>
  shows \<open>val1 = val2\<close>
proof -
  have \<open>states 0 = Some val1\<close>
    by (metis assms(1) assms(2) inv1_def inv2_def invariants)
  moreover have \<open>states 0 = Some val2\<close>
    by (metis assms(1) assms(3) inv1_def inv2_def invariants)
  ultimately show \<open>val1 = val2\<close>
    by simp
qed

end
