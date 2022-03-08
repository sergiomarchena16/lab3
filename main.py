import pefile

pe =  pefile.PE('MALWR/1F2EB7B090018D975E6D9B40868C94CA')
pe.OPTIONAL_HEADER.AddressOfEntryPoint
pe.OPTIONAL_HEADER.ImageBase
pe.FILE_HEADER.NumberOfSections

print(pe)
pe.FILE_HEADER.Machine

pe.DOS_HEADER.e_sp
