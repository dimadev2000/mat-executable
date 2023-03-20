#include <iostream>
#include "cgcustommath/cgcustommath.h"
#include <string>

int main(int argc, char* argv[]) {
  // check if there are two command line parameters
  if (argc != 3) {
    std::cerr << "Usage: " << argv[0] << " a b\n"; // print an error message
    return 1; // exit with non-zero status
  }

  // convert the command line parameters to integers
  int a = std::stoi(argv[1]); // convert the first parameter to int
  int b = std::stoi(argv[2]); // convert the second parameter to int

  // call the matrix function with a and b as arguments
  std::string result = matrix(a, b);

    // print the resulting array on screen using Eigen's IO format with 4 digits precision
  std::cout << result << "\n";

  return 0; // exit with zero status
}