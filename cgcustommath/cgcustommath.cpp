// cgcustommath.cpp : Defines the entry point for the application.
//

#include "cgcustommath.h"
#include <Eigen/Core>
#include <sstream>

std::string matrix(int a, int b) {
	Eigen::ArrayXXf m(2, 2);
	m.setZero();
	for (int i = 0; i < m.rows(); i++) {
  		m(i,i) = 1;
	}
	m *= a; // multiply the array by a
	m += b; // add b to the array
	std::stringstream ss;
	ss << m.format(Eigen::IOFormat(4));
	return ss.str(); // return the result
}
