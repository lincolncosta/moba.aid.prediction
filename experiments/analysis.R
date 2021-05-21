# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
# install if you do not have the packages in your R system

# uncomment the following line to install packages
# install.packages(c("ggplot2", "partykit"))

library(mlr)
library(ggplot2)

# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------

dir.create("../plots/")

# loading data
load(file = "./benchmarking_results.RData") #bmk


# --------------------------------------------------------------------------------------------------
# boxplots
# --------------------------------------------------------------------------------------------------

g1 = plotBMRBoxplots(bmk, measure = auc)
ggsave(g1, file = "../plots/bench_auc.pdf", width = 7.68, height = 3)

g2 = plotBMRBoxplots(bmk, measure = bac)
ggsave(g2, file = "../plots/bench_bac.pdf", width = 7.68, height = 3)

g3 = plotBMRBoxplots(bmk, measure = f1)
ggsave(g3, file = "../plots/bench_f1.pdf", width = 7.68, height = 3)


# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
