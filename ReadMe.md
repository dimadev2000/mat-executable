# Mat-Executable

`cgcustommath` has a function `Eigen::Array22f matrix(int a, int b)` and dependency on Eigen3 library managed through Conan
mat executable links to `cgcustommath`

## Prerequisites
Check conan version: `conan --verion` 
`Conan version 2.0.2` 

Check cmake version: `cmake --version`
`cmake version 3.26.0`

## Windows
Run `build_win.bat` to start downloading Eigen3 from conan, then build and install.
Run `python3 build_win_installer.py` to make an msi installer for application. After built run .\build\matexecutable.msi to install
Run `generate_vs.bat` to run cmake and download Eigen3 to local, then you can Open Project CMake in VS IDE and start debugging.

## MacOS
Run `build_mac.bat` to start downloading Eigen3 from conan, then build and install.
Run `python3 build_mac_íntaller.py` to make an dmg installer for application.
Run `generate_xcode.bat` to run cmake and download Eigen3 to local, then you can Open Project CMake in VS IDE and start debugging.
