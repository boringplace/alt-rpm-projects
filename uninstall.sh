#!/bin/bash
sed -i "s!\(%_topdir\s\+\).*!\1%homedir/RPM!" ~/.rpmmacros
