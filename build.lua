--[==========================================[--
         L3BUILD FILE FOR "PHY4804@CMT"
--]==========================================]--

module           = "PHY4804@CMT"
version          = "2025-12-01"
docsuppdirs      = {"context", "media"}
unpacksuppfiles  = {"*.bib"}
textfiles        = {"*.md", "LICENSE", "*.lua"}
typesetexe       = "latexmk"
typesetfiles     = {module .. ".tex"}
typesetopts      = "-pdf -interaction=nonstopmode"

function docinit_hook()
  for _,glob in pairs(docsuppdirs) do
    run(currentdir, "cp -r " .. glob .. " " .. typesetdir)
  end
  return 0
end
function tex(file,dir,cmd)
  dir = dir or "."
  cmd = cmd or typesetexe .. " " .. typesetopts
  return run(dir, cmd .. file)
end
