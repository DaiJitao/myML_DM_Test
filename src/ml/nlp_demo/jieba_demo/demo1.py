import jieba

import jpype # conda install -c conda-forge jpype1

from jpype import *
import os.path
startJVM(getDefaultJVMPath(), "-ea")
java.lang.System.out.println("hello World")
java.lang.System.out.println(getDefaultJVMPath())
shutdownJVM()