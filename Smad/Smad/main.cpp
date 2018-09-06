#include <stdio.h>
#include "Variant2DataGenerator.h"
#include "NormalDistributionGenerator.h"
#include "ConstRand.h"

const int tetaSize = 4;
const float tetaTable[tetaSize]
{
	1, 3, 1.f / 100, 1.f / 3
};

void main()
{
	RandomGenerator * rnd = new ConstRand(0);
	vector <float> tetaVec;
	for (int i = 0; i < tetaSize; i++)
	{
		tetaVec.push_back(tetaTable[i]);
	}

	Variant2DataGenerator dataGen(tetaVec, rnd);
	for (float i = -1; i <= 1; i += 0.125)
	{
		for (float j = -1; j <= 1; j += 0.125)
		{
			printf("%f\n", dataGen.generate({ j,i }));
		}
	}
	printf_s("Hello");

	delete rnd;
}