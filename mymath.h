#pragma once

#ifdef _WIN32
  #define mymath_EXPORT __declspec(dllexport)
#else
  #define mymath_EXPORT
#endif

mymath_EXPORT void mymath();
