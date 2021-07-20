#!/GPFS/zhangli_lab_permanent/zhuqingjie/env/py3_tf2/bin/python
'''
@Time    : 20/11/16 下午 06:45
@Author  : zhuqingjie 
@User    : zhu
@FileName: distit.py
@Software: PyCharm
'''
import os
import time
import shutil
import easyFlyTracker

'''
注意：需要安装两个库：
pip install wheel
pip install twine
'''

# delete cache files
shutil.rmtree('dist', ignore_errors=True)
shutil.rmtree('build', ignore_errors=True)
shutil.rmtree('easyFlyTracker.egg-info', ignore_errors=True)

time.sleep(0.5)
# 1，Generating distribution archives
os.system('python setup.py sdist bdist_wheel')

# time.sleep(0.5)
# # 2，Uploading the distribution archives
# os.system('twine upload --repository pypi dist/*')

ver = easyFlyTracker.__version__
print(
    f'''
Update:
pip install easyFlyTracker-{ver}-py3-none-any.whl
    '''
)