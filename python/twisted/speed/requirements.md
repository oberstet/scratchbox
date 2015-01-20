# Requirements

The following is a braindump/collection of requirements for a performance test system and infrastructure suitable for doing performance tests targeting Twisted.

1. A simple Twisted based "TCP echo server" (maybe in non-producer/consumer and producer/consumer variants) as a testee will already allow us to do a _lot_.
We can come up with more testees later (e.g. Twisted Web with static resource, ...).

2. It might be wise to use a non-Twisted, standard test load generator like netperf, instead of a Twisted based one.
   - having the load generator written in Twisted creates a cyclic dependency (e.g. rgd. interpreting results)
   - it allows to compare results to non-Twisted setups and allows others to repeat against their stuff

3. We should include at least 2 operating systems (FreeBSD / Linux).
This allows to quickly bisect OS or Twisted reactor specific issues.

4. We should run this on real, physical, non-virtualized, dedicated hardware and networking gear.
I can't stress enough how important this is in my experience:
Any form of virtualization brings a whole own dimension of factors/variability into the game.
Testing in VMs on a shared hypervisor on a public cloud: you never really know, you never really can repeat.
Repeatability is absolutely crucial.

5. The load generator and the testee should run on 2 separate boxes, connected via real network (e.g. switched ether).
Testing via loopback is often misleading, and practically often irrelevant (too far away from production deployments).

6. We should test on both CPython and PyPy.
Because this is where stuff actually runs later in production. And for bisecting Python implementation specifics.

7. It should be automated.

8. The results should be stored in a long term archive (a database) so we can compare results over time / setups.

9. We should collect monitoring parameters (CPU load ...) on both the load generator and testee boxes during test runs.
Like, "same network perf., but one triggers double the CPU load" ..

10. Changes to the test environment and infrastructure should be tracked (at least manually) - "a clearly documented log of operations performed on the monitoring cluster"

11. "the main reason we need a performance testing rig is not continuous performance monitoring over time, but rather, clear performance tracking of individual changes, ideally before they land"

12. "tell it to build a branch and get a good picture of the aggregate effect of that branch on the benchmarks"

13. ".. I need latency histograms .."

14. ".. latency heatmaps are awesome .."

15. "Keep in mind that a performance testing environment should be scalable.  Others may have different environments they care about.  Building your specific environment would be tremendously useful, but it would be even more useful to build it in a way that others can compare in their own hardware setups."

