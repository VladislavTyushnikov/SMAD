#pragma once
#include "RandomGenerator.h"

class NormalDistributionGenerator : public RandomGenerator
{
private:
	float m_sigma;
	float m_mu;
public:
	NormalDistributionGenerator(float sigma, float mu);
	float rand() const override;
	~NormalDistributionGenerator() override;
};