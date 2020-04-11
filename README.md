# Libsign
A IDAPython innocent script to find library copyright signatures

# What ?

This IDAPython script is made to find copyright, signature strings leaked by commun libs used in C and C++

This approch is not very clever because we can just search function patterns instead and get a more accurate result, but there is already a tool for that : [IDA Signsrch](https://github.com/nihilus/IDA_Signsrch)

The objective of this tool is to "find" the open source code behind it, to understand the limit of the library in the executable

The DB is not big, I just put signatures that I found in so executables, I highly recommend to use this with [IDA Signsrch](https://github.com/nihilus/IDA_Signsrch) to get more results

# Known signatures

- Deflate (zlib)
- Inflate (zlib)
- ZipArchive library (zlib)
- Zip (zlib)
- Unzip (zlib)
- Rar library
- Unrar library
- 7zip library
- JsonCpp
- JSON for Modern C++
- Lua library
- Python library
- SQLite library
- Libavcodec
- ImGui
