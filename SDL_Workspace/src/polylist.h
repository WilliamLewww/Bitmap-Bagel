#pragma once
#include "vector2.h"
#include "geometry.h"
#include <iostream>
#include <fstream>
#include <vector>

class Polylist {
	Vector2 position;
	std::vector<Vector2> vertices;

	int color[3] = { 50, 255, 100 };
	int alpha = 255;

public:
	inline void setVertices(const char* filename) {
		
	};

	inline void Draw() {
		//drawPolygon(position, vertices, color, alpha);
	};
};