#pragma once
#include "vector2.h"
#include <SDL2\SDL_opengl.h>
#include <vector>

double convertColor(int rgbValue);
void drawPoint(Vector2 position, int color[3]);
void drawPoint(Vector2 position, int color[3], int alpha);
void drawRect(Vector2 position, int width, int height);
void drawRect(Vector2 position, int width, int height, double angle);
void drawRect(Vector2 position, int width, int height, double angle, int color[3]);
void drawRect(Vector2 position, int width, int height, int color[3]);
void drawEdgesOfRect(Vector2 position, int width, int height, double angle, int color[3]);
void drawLine(Vector2 a, Vector2 b);
void drawLine(Vector2 a, Vector2 b, int color[3]);
void drawLine(Vector2 a, Vector2 b, int color[3], int alpha);
void drawLineStrip(std::vector<Vector2> points, int color[3]);
void drawLineStrip(Vector2 position, std::vector<Vector2> points, int color[3]);
void drawPolygon(std::vector<Vector2> points, int color[3], int alpha);
void drawPolygon(Vector2 position, std::vector<Vector2> vertices, int color[3], int alpha);
void drawCircle(Vector2 position, float radius);
void drawCircle(Vector2 position, float radius, int color[3]);
void drawTriangle(Vector2 position, int width, int height);
void drawTriangle(Vector2 position, int width, int height, double angle);