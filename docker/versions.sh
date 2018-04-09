#!/bin/sh

#
# CHANGE FOR NEW RELEASES (these need to be proper Git tags in the respective repo):
#
export CROSSBAR_VERSION='18.3.1'
export CROSSBAR_FABRIC_VERSION='18.3.1'
export AUTOBAHN_JS_VERSION='18.3.2'
export AUTOBAHN_PYTHON_VERSION='18.3.1'
export AUTOBAHN_CPP_VERSION='17.5.1'
export AUTOBAHN_JAVA_VERSION='17.10.5'
export AUTOBAHN_TESTSUITE_VERSION='0.7.6'
#
# END OF CONFIG
#

#
# Git working directories of all relevant repos must reside
# in parallel (as siblings) to this repository
#
export CROSSBAR_VCS_REF=`git --git-dir="../crossbar/.git" rev-list -n 1 v${CROSSBAR_VERSION} --abbrev-commit`
export CROSSBAR_FABRIC_VCS_REF="-"

export AUTOBAHN_JS_VCS_REF=`git --git-dir="../autobahn-js/.git" rev-list -n 1 v${AUTOBAHN_JS_VERSION} --abbrev-commit`
export AUTOBAHN_PYTHON_VCS_REF=`git --git-dir="../autobahn-python/.git" rev-list -n 1 v${AUTOBAHN_PYTHON_VERSION} --abbrev-commit`
export AUTOBAHN_CPP_VCS_REF=`git --git-dir="../autobahn-cpp/.git" rev-list -n 1 v${AUTOBAHN_CPP_VERSION} --abbrev-commit`
export AUTOBAHN_JAVA_VCS_REF="-"
export AUTOBAHN_TESTSUITE_VCS_REF=`git --git-dir="../autobahn-testsuite/.git" rev-list -n 1 v${AUTOBAHN_TESTSUITE_VERSION} --abbrev-commit`

export BUILD_DATE=`date -u +"%Y-%m-%d"`

echo ""
echo "The Crossbar.io Project (build date ${BUILD_DATE})"
echo ""
echo "crossbar ${CROSSBAR_VERSION} [${CROSSBAR_VCS_REF}]"
echo "crossbar-fabric ${CROSSBAR_FABRIC_VERSION} [${CROSSBAR_FABRIC_VCS_REF}]"
echo "autobahn-js ${AUTOBAHN_JS_VERSION} [${AUTOBAHN_JS_VCS_REF}]"
echo "autobahn-python ${AUTOBAHN_PYTHON_VERSION} [${AUTOBAHN_PYTHON_VCS_REF}]"
echo "autobahn-cpp ${AUTOBAHN_CPP_VERSION} [${AUTOBAHN_CPP_VCS_REF}]"
echo "autobahn-java ${AUTOBAHN_JAVA_VERSION} [${AUTOBAHN_JAVA_VCS_REF}]"
echo "autobahn-testsuite ${AUTOBAHN_TESTSUITE_VERSION} [${AUTOBAHN_TESTSUITE_VCS_REF}]"
echo ""
