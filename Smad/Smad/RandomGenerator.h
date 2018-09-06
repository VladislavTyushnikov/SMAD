#pragma once

class RandomGenerator
{
public:
	virtual const float rand() = 0;
	virtual ~RandomGenerator() {};
};