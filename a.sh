cd build/
make clean
cd ../
rm -r build 
mkdir build && cd build
cmake ..
make -j
./EdgeDirectVO