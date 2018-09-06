#pragma once
#include "ModelDataGenerator.h"

class Variant2DataGenerator : public ModelDataGenerator
{
private:

	float modelFunc(const vector<float> &vecX, const vector<float> &vecTeta) const override;

public:

	Variant2DataGenerator(const vector<float> &tetaVec, const RandomGenerator * rnd);
	~Variant2DataGenerator() override;

};