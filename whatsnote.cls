\def \whatsnote@date    {2025-11-10}
\def \whatsnote@version {v5.0A}
\ProvidesExplPackage {whatsnote} {\whatsnote@date} {\whatsnote@version}
  {LaTeX class for taking notes in science, engineering, etc.}
\catcode`\^^A 14\relax

\cs_new_protected:Npn \whatsnote_msg_new:nn #1#2 
  { \msg_new:nnn { whatsnote } {#1} {#2} }
\cs_new_protected:Npn \whatsnote_msg_error:nn #1#2
  { \msg_error:nnn { whatsnote } {#1} {#2} }
\cs_generate_variant:Nn \whatsnote_msg_error:nn { nx }
\whatsnote_msg_new:nn { not found module }
  { The ~ whats ~ module ~ `#1' ~ not ~ found. }
\cs_new_protected_nopar:Npn \whatsnote_provide_module:n #1
  {
    \ProvidesExplFile {Whats-#1-module.code.tex}
      {\whatsnote@date} {\whatsnote@version}
      { WhatsNote ~ \text_titlecase:n {#1} ~ Module }
  }
\cs_new_protected_nopar:Npn \whatsnote_load_module:n #1 
  {
    \clist_map_inline:nn {#1}
      {
        \file_if_exist_input:nF { Whats-##1-module.code.tex }
          { \whatsnote_msg_error:nn { not found module } {##1} }
      }
  }

% global options
\clist_new:N \g_@@_base_class_options_clist
\keys_define:nn { whats / classoption }
  {
    darkmode .bool_set:N    = \g_@@_darkmode_bool,
      darkmode .initial:n   = false,
      darkmode .default:n   = true,
    unknown .code:n         = \@@_unknown_option:n { #1 },
  }
\cs_new_protected_nopar:Npn \@@_unknown_option:n #1
  {
    \tl_if_empty:nTF { #1 }
      { \clist_gput_right:NV \g_@@_base_class_options_clist \l_keys_key_str }
      {
        \exp_args:NNx \clist_gput_right:Nn \g_@@_base_class_options_clist
          { \l_keys_key_str = \exp_not:n {#1} }
      }
  }
\ProcessKeyOptions [ whats / classoption ]
\PassOptionsToClass { book } { 11pt }
\PassOptionsToPackage { svgnames } { xcolor }
\exp_args:NNV \LoadClass [ \g_@@_base_class_options_clist ] { book }

\whatsnote_load_module:n { typeset, layout, cover }

\file_input_stop: