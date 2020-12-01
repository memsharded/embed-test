#pragma once

#ifdef WIN32
  #define myphsx_EXPORT __declspec(dllexport)
#else
  #define myphsx_EXPORT
#endif

myphsx_EXPORT void myphsx();
