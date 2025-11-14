--[==========================================[--
         L3BUILD FILE FOR "[PHY4804]CMT"
--]==========================================]--

module           = "CMT"
version          = "2025-11-16"
ctanzip          = module
excludefiles     = {"*~"}
suppdirs         = {"chapter", "media"}
unpacksuppfiles  = {"*.bib"}
textfiles        = {"*.md", "LICENSE", "*.lua"}
typesetexe       = "latexmk"
typesetfiles     = {module .. ".tex"}
typesetopts      = "-pdf -interaction=nonstopmode"

function docinit_hook()
  for _,supp in pairs(suppdirs) do
    run(currentdir, "cp -r " .. supp .. " " .. typesetdir)
  end
  return 0
end
function tex(file,dir,cmd)
  dir = dir or "."
  cmd = cmd or typesetexe .. " " .. typesetopts
  return run(dir, cmd .. file)
end
function copyctan()
  local pkgdir = ctandir .. "/" .. ctanpkg
  mkdir(pkgdir)
  for _,main in ipairs({typesetsuppfiles, pdffiles}) do
    for _,glob in pairs(main) do
      cp(glob, typesetdir, pkgdir)
    end
  end
  local pkgsuppdir = ctandir .. "/" .. ctanpkg .. "/" .. supportdir
  mkdir(pkgsuppdir)
  for _,supptab in pairs(typesetsuppfiles) do
    cp(supptab, supportdir, pkgsuppdir)
  end
end