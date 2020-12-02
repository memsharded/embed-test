#if WIN32
static volatile char* mydata = "OLA K ASE CARABOLO";
struct ForceFunctionToBeLinked
{
  ForceFunctionToBeLinked(const void *p) { SetLastError(PtrToInt(p)); }
};

ForceFunctionToBeLinked forceTestMe(TestMe);

#else
static volatile char mydata[] __attribute__((used)) = "OLA K ASE CARABOLO";
#endif