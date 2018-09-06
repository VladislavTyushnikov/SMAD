#include "Variant2DataGenerator.h"


Variant2DataGenerator::Variant2DataGenerator(const vector<float> &tetaVec, const RandomGenerator * rnd) :
	ModelDataGenerator(tetaVec, rnd)
{

}


float Variant2DataGenerator::modelFunc(const vector<float> &vecX, const vector<float> &vecTeta) const
{
	assert(vecX.size() == 2);
	assert(vecTeta.size() == 4);

	float x1 = vecX[0];
	float x2 = vecX[1];

	float y = vecTeta[0 ] * abs(x1) + vecTeta[1] * x2 * x2 + vecTeta[2] * sin(x1 * 50) + vecTeta[3] * sin (x2 * 10);
	return y;

}


Variant2DataGenerator::~Variant2DataGenerator()
{

}
