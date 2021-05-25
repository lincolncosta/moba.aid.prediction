# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
# install if you do not have the packages in your R system

# uncomment the following line to install packages
# install.packages(c("ggplot2", "PMCMR", "PMCMRplus", "dplyr"),
# repos = "http://cran.us.r-project.org")

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
ggsave(g1, file = "../plots/bench_auc.pdf", width = 7.97, height = 5.01)

g2 = plotBMRBoxplots(bmk, measure = bac)
ggsave(g2, file = "../plots/bench_bac.pdf", width = 7.97, height = 5.01)

g3 = plotBMRBoxplots(bmk, measure = f1)
ggsave(g3, file = "../plots/bench_f1.pdf", width = 7.97, height = 5.01)

# --------------------------------------------------------------------------------------------------
# Rf feature importance
# --------------------------------------------------------------------------------------------------

tasks = c("picked_champions", "players_statistics", "picked_champions_players_statistics",
  "banned_champions", "full")

# repeating the analysis for all the datasets
for(task in tasks) {

  cat("RF feature importance for: ", task, "\n")

  rf.models = mlr::getBMRModels(bmr=bmk, learner.ids = "RandomForest",
    task.ids = task, drop = TRUE)

  # feature importance
  aux = lapply(rf.models, function(mdl) {
    obj = mlr::getLearnerModel(mdl)
    return(obj$importance)
  })
  avg.imp = Reduce("+", aux)/length(aux)

  df = data.frame(avg.imp)
  df$feature = rownames(df)
  rownames(df) = NULL

  #ordering the factors
  df = df[order(df$MeanDecreaseGini, decreasing=TRUE),]
  df$feature = factor(df$feature, levels = df$feature)

  # bar plot
  g = ggplot(df, mapping = aes(x = feature, y = MeanDecreaseGini))
  g = g + geom_bar(stat = "identity", fill = "black") + theme_bw()
  g = g + theme(axis.text.x = element_text(angle = 90, vjust = .5, hjust = 1))

  ggsave(g, file = paste0("../plots/rf_feature_importance_", task, "_.pdf"),
    width = 6.89, height = 3.04)
}

# --------------------------------------------------------------------------------------------------
# Plot critical difference test for a selected measure
# --------------------------------------------------------------------------------------------------

obj = mlr::generateCritDifferencesData(bmr = bmk, measure = auc, p.value = 0.05, test = "nemenyi")
g2  = mlr::plotCritDifferences(obj = obj)

ggsave(g2, file = "../plots/cd_nemenyi.pdf", width = 6.95, height = 2.67)



# --------------------------------------------------------------------------------------------------
#  customized boxplots
# --------------------------------------------------------------------------------------------------

perfs = getBMRPerformances(bmr = bmk, as.df = TRUE)
measures = c("auc", "bac", "f1")
colnames(perfs)[1:2] = c("Task", "Learner")

# Renaming task factors
perfs$Task = dplyr::recode_factor(perfs$Task,
  banned_champions = "Banned Champions",
  full = "Complete",
  picked_champions = "Picked Champions",
  picked_champions_players_statistics = "Picked Champions and\n Players Statistics",
  players_statistics = "Players Statistics")

perfs$Task = factor(perfs$Task, levels = c("Banned Champions", "Picked Champions",
  "Players Statistics", "Picked Champions and\n Players Statistics", "Complete"))

# Renaming learner factors
perfs$Learner = dplyr::recode_factor(perfs$Learner,
  RandomForest = "RF", Rpart = "DT", SVM = "SVM",
  LogReg = "LR", NaiveBayes = "NB", KKNN = "kNN")

# Reordeing learner factors
perfs$Learner = factor(perfs$Learner, levels = c("DT", "NB", "kNN",
  "SVM", "RF", "LR"))

# Plot AUC
sel = c("Task", "Learner", "iter", "auc")
sub = perfs[, sel]
g = ggplot(data = sub, mapping = aes(x = Learner, y = auc))
g = g + geom_boxplot() + facet_grid(.~Task) + theme_bw()
g = g + theme(axis.text.x = element_text(angle = 90, vjust = .5, hjust = 1))
ggsave(g, file = "../plots/customized_boxplot_auc.pdf", width = 8.17, height = 2.37)

# Plot BAC
sel = c("Task", "Learner", "iter", "bac")
sub = perfs[, sel]
g = ggplot(data = sub, mapping = aes(x = Learner, y = bac))
g = g + geom_boxplot() + facet_grid(.~Task) + theme_bw()
g = g + theme(axis.text.x = element_text(angle = 90, vjust = .5, hjust = 1))
ggsave(g, file = "../plots/customized_boxplot_bac.pdf", width = 8.17, height = 2.37)

# Plot BAC
sel = c("Task", "Learner", "iter", "f1")
sub = perfs[, sel]
g = ggplot(data = sub, mapping = aes(x = Learner, y = f1))
g = g + geom_boxplot() + facet_grid(.~Task) + theme_bw()
g = g + theme(axis.text.x = element_text(angle = 90, vjust = .5, hjust = 1))
ggsave(g, file = "../plots/customized_boxplot_f1.pdf", width = 8.17, height = 2.37)

# --------------------------------------------------------------------------------------------------
# PCA plot
# --------------------------------------------------------------------------------------------------

# dataset = read.csv("../data/dataset_picked_champions_players_statistics.csv")
#
# target = dataset$result
#
# df = dataset[,-c(1,2)]
# df$result = NULL
#
#
# objPCA = prcomp(df, scale = TRUE)
#
# objPCA = prcomp(df)
#
# dfOut = as.data.frame(objPCA$x)
# dfOut$target = target
#
# p = ggplot(dfOut,aes(x=PC1,y=PC2,color=target ))
# p = p + geom_point()
# p


# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
