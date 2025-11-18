///// DispatchProbe.proto /////

static CYTHON_INLINE void __Pyx_TrySetupCDispatcher(void);


///// DispatchProbe /////

static CYTHON_INLINE void __Pyx_TrySetupCDispatcher(void) {
    /* Optional integration point for an external multi-backend dispatcher.
       In this fork, we provide a no-op stub so that generated modules
       compile cleanly even when no dispatcher library is present. */
}



