#pragma once

class RandomGenerator
{
public:
	virtual float rand() const = 0;
	virtual ~RandomGenerator() {};
};