#include "ConstRand.h"

ConstRand::ConstRand(float genConst):
	m_genConst(genConst)
{

}
float ConstRand::rand() const
{
	return m_genConst;
}

ConstRand::~ConstRand() {};