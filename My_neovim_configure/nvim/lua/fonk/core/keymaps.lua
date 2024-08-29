vim.g.mapleader = " "

local keymap = vim.keymap

keymap.set("i", "jj", "<ESC>")
keymap.set("n", "Q", ":wq<CR>")

keymap.set("v", "J", ":m '>+1<CR>gv+gv")
keymap.set("v", "K", ":m '<-2<CR>gv+gv")

keymap.set("n", "<leader>nh", ":nohl<CR>")

keymap.set("n", "<leader>e" , ":Neotree toggle<CR>")

