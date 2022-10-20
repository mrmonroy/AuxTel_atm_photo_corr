# README.md PhotomCorrectAuxTel/tools/libradtran

- creation date : December 13th 2021


Notebooks tools to check if libratran installation is working well



## Notebooks for control of libradtran or examples

-**SimuRT_py3.ipynb**: Generic libradtran test , including clouds extinction


-**SimuRT_vsairmass_py3.ipynb**: libradtran test wrt airmass


-**SimuRT_AbsPattern_py3.ipynb**: Simulate only the absorption only


-**SimuRT_Verbose_py3.ipynb**: To be used only if one need to work libradtran in verbose mode : only one vertical profile is generated. Must put verbose mode in **libsimulateVisible.py** by hand


## base interface libraries to libradtran


- **libsimulateVisible.py** : interface library used for LSST
- **libsimulateVisible_pdm.py** : interface library for Pic Du Midi Observatory   
- **UVspec3.py** : low level library used by    **libsimulateVisible.py**  and **libsimulateVisible_pdm.py**
