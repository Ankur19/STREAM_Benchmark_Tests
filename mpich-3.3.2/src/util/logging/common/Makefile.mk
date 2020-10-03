## -*- Mode: Makefile; -*-
## vim: set ft=automake :
##
## (C) 2011 by Argonne National Laboratory.
##     See COPYRIGHT in top-level directory.
##

## this code is commented out in the old Makefile.sm, so we leave it here but
## similarly disabled
##mpi_core_sources +=   \
##    describe_states.c

AM_CPPFLAGS += -I$(top_srcdir)/src/util/logging/common

# FIXME XXX DJG this file is autogenerated, right?  how do we correctly express
# the dependency on the "extractstates" generator code?
noinst_HEADERS += src/util/logging/common/state_names.h