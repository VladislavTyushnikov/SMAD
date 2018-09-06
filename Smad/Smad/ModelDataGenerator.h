#pragma once
#include<vector>
#include "RandomGenerator.h"
#include <assert.h>
using namespace std;

class ModelDataGenerator
{
protected:

	vector<float> m_tetaVec;
	const RandomGenerator * m_rnd;

	float virtual modelFunc(const vector<float> &vecX, const vector<float> &vecTeta) const = 0;

public:

	ModelDataGenerator(const vector<float> &tetaVec, const RandomGenerator * rnd);

	float generate(const vector<float> &x) const;

	virtual ~ModelDataGenerator();
};