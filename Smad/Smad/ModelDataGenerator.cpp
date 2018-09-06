#include "ModelDataGenerator.h"



ModelDataGenerator::ModelDataGenerator(const vector<float> &tetaVec, const RandomGenerator * rnd) :
	m_tetaVec(tetaVec),
	m_rnd(rnd)
{

}

float ModelDataGenerator::generate(const vector<float> &x) const
{
	float y = modelFunc(x, m_tetaVec);
	return y + m_rnd->rand();
}


ModelDataGenerator::~ModelDataGenerator()
{

}