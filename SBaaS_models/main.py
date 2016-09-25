import sys
sys.path.append('C:/Users/dmccloskey-sbrg/Documents/GitHub/SBaaS_base')
#sys.path.append('C:/Users/dmccloskey/Documents/GitHub/SBaaS_base')
from SBaaS_base.postgresql_settings import postgresql_settings
from SBaaS_base.postgresql_orm import postgresql_orm

# read in the settings file
filename = 'C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_settings/settings_metabolomics.ini';
#filename = 'C:/Users/dmccloskey/Google Drive/SBaaS_settings/settings_metabolomics_labtop.ini';
pg_settings = postgresql_settings(filename);

# connect to the database from the settings file
pg_orm = postgresql_orm();
pg_orm.set_sessionFromSettings(pg_settings.database_settings);
session = pg_orm.get_session();
engine = pg_orm.get_engine();

# your app...
# SBaaS paths:
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_base')
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_models')
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_LIMS')
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_COBRA')
# SBaaS dependencies paths:
sys.path.append(pg_settings.datadir_settings['github']+'/io_utilities')
sys.path.append(pg_settings.datadir_settings['github']+'/python_statistics')
sys.path.append(pg_settings.datadir_settings['github']+'/r_statistics')
sys.path.append(pg_settings.datadir_settings['github']+'/listDict')
sys.path.append(pg_settings.datadir_settings['github']+'/ddt_python')
sys.path.append(pg_settings.datadir_settings['github']+'/molmass')
sys.path.append(pg_settings.datadir_settings['github']+'/genomeScale_MFA')
sys.path.append(pg_settings.datadir_settings['github']+'/genomeScale_MFA_INCA')

#make the COBRA table
from SBaaS_models.models_COBRA_execute import models_COBRA_execute
cobra01 = models_COBRA_execute(session,engine,pg_settings.datadir_settings);
cobra01.initialize_supportedTables()
cobra01.initialize_tables()

#make the BioCyc table
from SBaaS_models.models_BioCyc_execute import models_BioCyc_execute
biocyc01 = models_BioCyc_execute(session,engine,pg_settings.datadir_settings);
biocyc01.initialize_supportedTables()
biocyc01.initialize_tables()

#genes tested: 'tpiA','gloA','nrdA','mgsA','pfkA'
#biocyc01.export_geneRegulators_js('icd','ECOLI');
#biocyc01.export_geneReactions_js('icd','ECOLI');
#biocyc01.export_geneEnzymaticReactions_js('icd','ECOLI');
#biocyc01.export_geneRegulators_js('fli%','ECOLI');
#biocyc01.export_geneRegulatedEntities_js('spf','ECOLI');
#biocyc01.export_geneProteinFeatures_js('zwf','ECOLI');

#biocyc01.export_geneAndMetaboliteRegulatedEntities_sankeyDiagram_js(
#    genes_I=['soxR','soxS','oxyR','oxyS','marA','rob'],
#    metabolites_I = ['putrescine'],
#    database_I = 'ECOLI');
#biocyc01.export_geneTranscriptionUnitRegulators_sankeyDiagram_js(
#    genes_I=['glnE'],
#    database_I = 'ECOLI');

#biocyc01.export_geneReactionAndEnzymaticReactionRegulators_sankeyDiagram_js(
#    genes_I=['glnD'],
#    database_I = 'ECOLI');

#biocyc01.export_geneReactions_forceDirectedGraph_js(
#    genes_I=['glnL','glnG','glnB','glnD','glnE','glnK','glnA'],
#    database_I = 'ECOLI');
#biocyc01.export_geneReactionsAndEnzymaticReactions_forceDirectedGraph_js(
#    genes_I=['glnL','glnG','glnB','glnD','glnE','glnK','glnA'],
#    database_I = 'ECOLI');

#stringList_I = 'gadA,gadX,gadB,gadC'
#str_list = stringList_I.split(',');
#biocyc01.export_geneParentClasses_js(str_list,'ECOLI');

#stringList_I = 'bglG,bglGFB,leuO,molR_1,sfsB,yecT,ygiZ,yidL,ykiA,ynbABCD,ynjI,yqhG,adiC,aslB,cadBA,gadAX,slp-dctR,yhiM,csgDEFG,flhDC,rcsA,wza-wzb-wzc-wcaAB,yjbE,yjbEFGH'
#str_list = stringList_I.split(',');
#biocyc01.export_transcriptionUnitParentClassesHistogram_js(str_list,'ECOLI',single_plot_I=True);

#biocyc01.export_GOTermGenes_js('GO:0046034','ECOLI');

#biocyc01.getJoin_regulatorsAndRegulatedEntities_database_modelsBioCycRegulationAndAll('ECOLI')

super_pathways = [
    #Amino Acids Biosynthesis
    'superpathway of aromatic amino acid biosynthesis',
    'superpathway of branched chain amino acid biosynthesis',
    'superpathway of L-aspartate and L-asparagine biosynthesis',
    'superpathway of L-lysine, L-threonine and L-methionine biosynthesis I',
    'superpathway of L-serine and glycine biosynthesis I',

    ];
#data_O = [];
#for sp in super_pathways:
#    biocyc_pathways = biocyc01.getParsed_genesAndPathwaysAndReactions_superPathwayAndDatabase_modelsBioCycPathways(
#        super_pathway_I=sp,
#        database_I='ECOLI',
#        query_I={},
#        output_O='listDict',
#        dictColumn_I=None);
#    data_O.extend(biocyc_pathways);


#Part 1: query and map the network components to the measured data

#define the pathways
pathways = [
    #Amines and Polyamines Biosynthesis
    'glycine betaine biosynthesis I (Gram-negative bacteria)',
    'aminopropylcadaverine biosynthesis',
    'glutathionylspermidine biosynthesis',
    'putrescine biosynthesis I',
    'putrescine biosynthesis III',
    'spermidine biosynthesis I',
    'UDP-<i>N</i>-acetyl-D-glucosamine biosynthesis I',
    #Amino Acids Biosynthesis
    'glycine biosynthesis I',
    'L-alanine biosynthesis I',
    'L-alanine biosynthesis II',
    'L-alanine biosynthesis III',
    'L-arginine biosynthesis I (via L-ornithine)',
    'L-asparagine biosynthesis I',
    'L-asparagine biosynthesis II',
    'L-aspartate biosynthesis',
    'L-cysteine biosynthesis I',
    'L-glutamate biosynthesis I',
    'L-glutamate biosynthesis III',
    'L-glutamine biosynthesis I',
    'L-histidine biosynthesis',
    'L-isoleucine biosynthesis I (from threonine)',
    'L-leucine biosynthesis',
    'L-lysine biosynthesis I',
    'L-homoserine and L-methionine biosynthesis',
    'L-methionine biosynthesis I',
    'L-phenylalanine biosynthesis I',
    'L-proline biosynthesis I',
    'L-selenocysteine biosynthesis I (bacteria)',
    'L-serine biosynthesis',
    'L-threonine biosynthesis',
    'L-tryptophan biosynthesis',
    'L-tyrosine biosynthesis I',
    'L-valine biosynthesis',
    '&beta;-alanine biosynthesis III',
    'L-ornithine biosynthesis I',
    #Nucleosides and Nucleotides Biosynthesis
    'adenosine deoxyribonucleotides <i>de novo</i> biosynthesis II',
    'guanosine deoxyribonucleotides <i>de novo</i> biosynthesis II',
    'pyrimidine deoxyribonucleotides <i>de novo</i> biosynthesis I',
    'pyrimidine deoxyribonucleotides <i>de novo</i> biosynthesis II',
    '5-aminoimidazole ribonucleotide biosynthesis I',
    '5-aminoimidazole ribonucleotide biosynthesis II',
    'superpathway of 5-aminoimidazole ribonucleotide biosynthesis',
    'adenosine ribonucleotides <i>de novo</i> biosynthesis',
    'guanosine ribonucleotides <i>de novo</i> biosynthesis',
    #"inosine-5\'-phosphate biosynthesis I",
    #Fatty Acid and Lipid Biosynthesis
    '(Kdo)<sub>2</sub>-lipid A biosynthesis I',
    'biotin-carboxyl carrier protein assembly',
    'Lipid A-core biosynthesis',
    'lipid IV<sub>A</sub> biosynthesis',
    'fatty acid biosynthesis initiation I',
    'fatty acid biosynthesis initiation II',
    'fatty acid biosynthesis initiation III',
    'fatty acid elongation -- saturated',
    'cyclopropane fatty acid (CFA) biosynthesis',
    'palmitate biosynthesis II (bacteria and plants)',
    '(5Z)-dodec-5-enoate biosynthesis',
    '<i>cis</i>-vaccenate biosynthesis',
    'palmitoleate biosynthesis I (from (5Z)-dodec-5-enoate)',
    'Kdo transfer to lipid IV<sub>A</sub> I',
    'cardiolipin biosynthesis I',
    'cardiolipin biosynthesis III',
    'CDP-diacylglycerol biosynthesis I',
    'CDP-diacylglycerol biosynthesis II',
    'phosphatidylethanolamine biosynthesis I',
    #Cofactors, Prosthetic Groups, Electron Carriers Biosynthesis
    'acyl carrier protein metabolism',
    'cytidylyl molybdenum cofactor biosynthesis',
    'guanylyl molybdenum cofactor biosynthesis',
    'S-adenosyl-L-methionine biosynthesis',
    'tetrahydromonapterin biosynthesis',
    'coenzyme A biosynthesis I',
    'pantothenate and coenzyme A biosynthesis I',
    'lipoate biosynthesis and incorporation I',
    'lipoate biosynthesis and incorporation II',
    'molybdenum cofactor biosynthesis',
    'NAD biosynthesis I (from aspartate)',
    'di-<i>trans</i>,poly-<i>cis</i>-undecaprenyl phosphate biosynthesis',
    'octaprenyl diphosphate biosynthesis',
    'polyisoprenoid biosynthesis (<i>E. coli</i>)',
    '<i>trans, trans</i>-farnesyl diphosphate biosynthesis',
    'siroheme biosynthesis',
    'heme biosynthesis I (aerobic)',
    'heme biosynthesis II (anaerobic)',
    '1,4-dihydroxy-2-naphthoate biosynthesis',
    'demethylmenaquinol-8 biosynthesis I',
    'menaquinol-8 biosynthesis',
    'ubiquinol-8 biosynthesis (prokaryotic)',
    'glutathione biosynthesis',
    'glutathionylspermidine biosynthesis',
    'tetrapyrrole biosynthesis I (from glutamate)',
    'biotin biosynthesis from 8-amino-7-oxononanoate I',
    'biotin biosynthesis I',
    '8-amino-7-oxononanoate biosynthesis I',
    'adenosylcobalamin salvage from cobinamide I',
    'flavin biosynthesis I (bacteria and plants)',
    '4-aminobenzoate biosynthesis',
    '<i>N</i><sup>10</sup>-formyl-tetrahydrofolate biosynthesis',
    'folate polyglutamylation',
    'tetrahydrofolate biosynthesis',
    'phosphopantothenate biosynthesis I',
    '4-amino-2-methyl-5-diphosphomethylpyrimidine biosynthesis',
    'thiamine diphosphate biosynthesis I (E. coli)',
    'thiazole biosynthesis I (facultative anaerobic bacteria)',
    #"pyridoxal 5\'-phosphate biosynthesis I",
    #Cell Structures Biosynthesis
    'enterobacterial common antigen biosynthesis',
    ##Cell Wall
    'peptidoglycan biosynthesis I (<I>meso</I>-diaminopimelate containing)',
    'peptidoglycan maturation (<i>meso</i>-diaminopimelate containing)',
    'UDP-<i>N</i>-acetylmuramoyl-pentapeptide biosynthesis I (<i>meso</i>-diaminopimelate containing)',
    ##Lipopolysaccharide Biosynthesis
    '<i>O</i>-antigen building blocks biosynthesis (<i>E. coli</i>)',
    'dTDP-<i>N</i>-acetylthomosamine biosynthesis',
    'dTDP-L-rhamnose biosynthesis I',
    'UDP-&alpha;-D-glucuronate biosynthesis (from UDP-glucose)',
    'UDP-<i>N</i>-acetyl-&alpha;-D-mannosaminouronate biosynthesis',
    'UDP-<i>N</i>-acetyl-D-glucosamine biosynthesis I',
    #Carbohydrates Biosynthesis
    'colanic acid building blocks biosynthesis',
    'CMP-3-deoxy-D-<I>manno</I>-octulosonate biosynthesis',
    'glycogen biosynthesis I (from ADP-D-Glucose)',
    'ADP-L-<i>glycero</i>-&beta;-D-<i>manno</i>-heptose biosynthesis',
    'dTDP-L-rhamnose biosynthesis I',
    'dTDP-<i>N</i>-acetylthomosamine biosynthesis',
    'GDP-L-fucose biosynthesis I (from GDP-D-mannose)',
    'GDP-mannose biosynthesis',
    'UDP-&alpha;-D-glucuronate biosynthesis (from UDP-glucose)',
    'UDP-<i>N</i>-acetyl-&alpha;-D-mannosaminouronate biosynthesis',
    'UDP-D-galactose biosynthesis',
    'UDP-glucose biosynthesis',
    'trehalose biosynthesis I'
    ];
biocyc_pathways = biocyc01.getParsed_genesAndPathwaysAndReactions_namesAndDatabase_modelsBioCycPathways(
    names_I=pathways,
    database_I='ECOLI',
    query_I={},
    output_O='listDict',
    dictColumn_I=None);
genes = list(set([g['gene'] for g in biocyc_pathways if g['gene']!='']));
#join list of genes with alternative identifiers
biocyc_genes = biocyc01.getParsed_genesAndAccessionsAndSynonyms_namesAndDatabase_modelsBioCycPolymerSegments(
    names_I=genes,
    database_I='ECOLI',
    query_I={},
    output_O='listDict',
    dictColumn_I=None);
gene_ids = list(set(genes + [g['synonym'] for g in biocyc_genes if g['synonym']]));
accession_1 = list(set([g['accession_1'] for g in biocyc_genes if g['accession_1']!='']));
#Join accession_1 with COBRA reactions
cobra_rxnIDs = cobra01.get_rows_modelIDAndOrderedLocusNames_dataStage02PhysiologyModelReactions(
    model_id_I='150526_iDM2015',
    ordered_locus_names_I=accession_1,
    query_I={},
    output_O='listDict',
    dictColumn_I=None)
rxn_ids = list(set([g['rxn_id'].replace('_reverse','') for g in cobra_rxnIDs if g['rxn_id']!='']));

#COBRA metabolites
met_ids = list(set([p for g in cobra_rxnIDs if g['products_ids'] for p in g['products_ids']]+\
    [p for g in cobra_rxnIDs if g['reactants_ids'] for p in g['reactants_ids']]));
#deformat met_ids
from SBaaS_models.models_COBRA_dependencies import models_COBRA_dependencies
cobra_dependencies = models_COBRA_dependencies();
met_ids_deformated = list(set([cobra_dependencies.deformat_metid(m) for m in met_ids]));


#Part 2: query the measured data for each analysis

#Query gene expression levels using gene or synonyms
#...gene_ids

#Query rxn_id flux levels
#...rxn_ids
growth_rates = [];
#...

#Query met_id metabolite concentrations
#...met_ids_deformated

print('end main');