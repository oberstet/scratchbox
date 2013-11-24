# GitHub Workflow for Twisted Contributors

1. Go to the Twisted Git [repository](https://github.com/twisted/twisted) on GitHub and fork it.

2. Clone your forked repository and add upstream

		git clone git@github.com:oberstet/twisted.git
		cd twisted
		git remote add upstream git@github.com:twisted/twisted.git

3. Update to latest upstream changes (repeat that before you start working on something):

		git fetch --all
		git checkout trunk
		git merge upstream/trunk
		git push origin trunk

4. Create an issue/feature branch before starting your work:

		git checkout -b fix_6846

5. Now do your stuff and test:

		python ./bin/trial twisted.test.test_log.FileObserverTestCase.test_getTimezoneOffset

6. When done, add changes and commit:

		git add .
		git commit -m "fix #6846"
		git push origin fix_6846

7. To create a patch, get the ID of latest commit *before* your change:

		git log -n 2

8. .. and then create the patch:

		git diff 5a70d33377ea96814 > fix_6846.patch

9. To verify that the patch applies cleanly and actually works:

		git checkout trunk
		patch -p1 < fix_6846.patch
		python ./bin/trial twisted.test.test_log.FileObserverTestCase.test_getTimezoneOffset

10. Upload your `fix_6846.patch` to the Trac issue page, add the `review` keyword and assign to reviewer.

11. Cleanup

		git reset --hard
		rm fix_6846.patch
		rm twisted/test/test_log.py.orig

# Trials

You need to be sure which `trial` your run, and what Python that `trial` is using.

E.g.

	[bbslave_twisted@tvd_build_txpypy ~/scm/twisted]$ less ./bin/trial
	#!/usr/bin/env python

will run trial from the repo, but under the environment Python found for `python`.

This may or may not be what you want. Hence it is safe to force the actual Python to be used:

	[bbslave_twisted@tvd_build_txpypy ~/scm/twisted]$ which pypy2.2
	/home/bbslave_twisted/local/bin/pypy2.2
	[bbslave_twisted@tvd_build_txpypy ~/scm/twisted]$ pypy2.2 ./bin/trial ..

Regarding

	pypy2.2 ./bin/trial --reporter=bwverbose --reactor=select twisted.conch
	pypy2.2 ./bin/trial --reporter=bwverbose --reactor=kqueue twisted.test.test_iutils.ProcessUtilsTests

# PyPy Issues

	twisted.internet.test.test_tcp.SimpleUtilityTestCase.test_resolveIPv6

	twisted.python.test.test_reflectpy3.AccumulateMethodsTests.test_baseClass
	twisted.python.test.test_reflectpy3.AccumulateMethodsTests.test_ownClass
	twisted.python.test.test_reflectpy3.PrefixedMethodsTests.test_onlyObject

	twisted.test.test_pb.BrokerTestCase.test_cache
	twisted.test.test_pb.BrokerTestCase.test_refcount
	twisted.test.test_pb.NewCredTestCase.test_logoutAfterDecref

	twisted.trial.test.test_tests.TestUnhandledDeferred.test_isReported

	twisted.internet.test.test_process.PTYProcessTestsBuilder_KQueueReactor.test_openFileDescriptors
	twisted.internet.test.test_process.PTYProcessTestsBuilder_KQueueReactor.test_processExitedWithSignal
	twisted.internet.test.test_process.ProcessTestsBuilder_KQueueReactor.test_write

	twisted.python.test.test_fakepwd.ShadowDatabaseTests.test_noSuchName

	twisted.test.test_log.FileObserverTestCase.test_getTimezoneOffset

	twisted.test.test_plugin.DeveloperSetupTests.test_freshPyReplacesStalePyc
	twisted.test.test_plugin.DeveloperSetupTests.test_freshPyReplacesStalePyc

	twisted.test.test_rebuild.RebuildTestCase.testFileRebuild
	twisted.test.test_rebuild.NewStyleTestCase.test_slots
	
