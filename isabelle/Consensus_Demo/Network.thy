section \<open>Network model\<close>

text \<open>We define a simple model of a distributed system. The system consists of
a set of processes, each of which has a unique identifier and local state that
it can update. There is no shared state between processes; processes can
communicate only by sending messages to each other. The communication is
\emph{asynchronous} -- that is, messages may be delayed arbitrarily,
reordered, duplicated, or dropped entirely.

In reality, processes execute concurrently, possibly at different speeds (in
particular, a process may fail by stopping execution entirely). To model this,
we say that the system as a whole makes progress by one of the processes
performing an execution step, and processes may perform steps in any order.

An execution step involves a process handling an \emph{event}. An event could
be one of several things: a request from a user, receiving a message from
another process, or the elapsing of a timeout. In response to such an event,
a process can update its local state, and/or send messages to other processes.\<close>

theory
  Network
imports
  Main
begin


text \<open>A message is always sent to a particular recipient. This datatype
encapsulates the name of the recipient process and the message being sent.\<close>

datatype ('proc, 'msg) send
  = Send (msg_recipient: 'proc) (send_msg: 'msg)


text \<open>An event that a process may handle: receiving a message from another
process, or a request from a user, or an elapsed timeout.\<close>

datatype ('proc, 'msg, 'val) event
  = Receive (msg_sender: 'proc) (recv_msg: 'msg)
  | Request 'val
  | Timeout


text \<open>A step function takes three arguments: the name of the process that is
executing, its current local state, and the event being handled. It returns two
things: the new local state, and a set of messages to send to other processes.\<close>

type_synonym ('proc, 'state, 'msg, 'val) step_func =
  \<open>'proc \<Rightarrow> 'state \<Rightarrow> ('proc, 'msg, 'val) event \<Rightarrow> ('state \<times> ('proc, 'msg) send set)\<close>


text \<open>A process may only receive a message from a given sender if that sender
process did previously send that message. Request and Timeout events can occur
at any time.\<close>

fun valid_event :: \<open>('proc, 'msg, 'val) event \<Rightarrow> 'proc \<Rightarrow>
                    ('proc \<times> ('proc, 'msg) send) set \<Rightarrow> bool\<close> where
  \<open>valid_event (Receive sender msg) proc msgs = ((sender, Send proc msg) \<in> msgs)\<close> |
  \<open>valid_event (Request _) _ _ = True\<close> |
  \<open>valid_event Timeout _ _ = True\<close>


text \<open>A valid execution of a distributed algorithm is a sequence of execution
steps. At each step, any of the processes handles any valid event. We call the
step function to compute the next state for that process, and any messages it
sends are added to a global set of all messages ever sent.\<close>

inductive execute ::
    \<open>('proc, 'state, 'msg, 'val) step_func \<Rightarrow> ('proc \<Rightarrow> 'state) \<Rightarrow> 'proc set \<Rightarrow>
     ('proc \<times> ('proc, 'msg, 'val) event) list \<Rightarrow>
     ('proc \<times> ('proc, 'msg) send) set \<Rightarrow> ('proc \<Rightarrow> 'state) \<Rightarrow> bool\<close> where
  \<open>execute step init procs [] {} init\<close> |
  \<open>\<lbrakk>execute step init procs events msgs states;
    proc \<in> procs;
    valid_event event proc msgs;
    step proc (states proc) event = (new_state, sent);
    events' = events @ [(proc, event)];
    msgs' = msgs \<union> ((\<lambda>msg. (proc, msg)) ` sent);
    states' = states (proc := new_state)
   \<rbrakk> \<Longrightarrow> execute step init procs events' msgs' states'\<close>


subsection \<open>Lemmas for the network model\<close>

text \<open>We prove a few lemmas that are useful when working with the above network model.\<close>

inductive_cases execute_indcases: \<open>execute step init procs events msg states\<close>

lemma execute_init:
  assumes \<open>execute step init procs [] msgs states\<close>
  shows \<open>msgs = {} \<and> states = init\<close>
  using assms by(auto elim: execute.cases)

inductive_cases execute_snocE [elim!]:
  \<open>execute step init procs (events @ [(proc, event)]) msgs' states'\<close>

lemma execute_step:
  assumes \<open>execute step init procs (events @ [(proc, event)]) msgs' states'\<close>
  shows \<open>\<exists>msgs states sent new_state.
          execute step init procs events msgs states \<and>
          proc \<in> procs \<and>
          valid_event event proc msgs \<and>
          step proc (states proc) event = (new_state, sent) \<and>
          msgs' = msgs \<union> ((\<lambda>msg. (proc, msg)) ` sent) \<and>
          states' = states (proc := new_state)\<close>
  using assms by auto

lemma execute_receive:
  assumes \<open>execute step init procs (events @ [(recpt, Receive sender msg)]) msgs' states'\<close>
  shows \<open>(sender, Send recpt msg) \<in> msgs'\<close>
  using assms execute_step by fastforce

end
