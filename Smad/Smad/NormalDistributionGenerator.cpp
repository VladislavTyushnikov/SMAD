#include "NormalDistributionGenerator.h"

NormalDistributionGenerator::NormalDistributionGenerator(float sigma, float mu) :
	m_sigma(sigma),
	m_mu(mu)
{

}

float NormalDistributionGenerator::rand() const
{
	return 0;
}

NormalDistributionGenerator::~NormalDistributionGenerator()
{

}