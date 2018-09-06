#pragma once
#include "RandomGenerator.h"

class ConstRand : public RandomGenerator
{
private:
	float m_genConst;
public:
	ConstRand(float genConst);
	float rand() const override;
	~ConstRand() override;
};