# create your venv folder
from site import venv

from unittest.test.test_result import m

from tensorflow import python

python -m venv venv
call venv/Scripts/activate.bat

# install your requirements
pip install -r requirements_gpu.txt

# install the tf-openpose lib
# ref: https://github.com/ildoonet/tf-pose-estimation#install-1
git clone https://github.com/ildoonet/tf-pose-estimation.git
cd tf-openpose
python setup.py install
cd tf_pose/pafprocess
swig -python -c++ pafprocess.i && python3 setup.py build_ext --inplace
