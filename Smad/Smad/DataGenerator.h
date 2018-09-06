#pragma once
#include<vector>
#include "RandomGenerator.h"
using namespace std;

class DataGenerator
{
protected:

	float virtual modelFunc(const vector<float> &vecX, const vector<float> &vecTeta);

public:

	DataGenerator(const vector<float> &tetaVec, const RandomGenerator * rnd, const vector<float[2]> &xBorders);

	float generate(vector<float> x);
	bool setTetaVec(const vector<float> &newTeteVec);

	virtual ~DataGenerator();
};