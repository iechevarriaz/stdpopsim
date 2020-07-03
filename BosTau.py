"""
Catalog definitions for Bos Taurus
"""
import math
import logging

import msprime

import stdpopsim

logger = logging.getLogger(__name__)

###########################################################
#
# Genome definition
#
###########################################################


# Create a string of chromosome lengths for easy parsing
_chromosome_data = """\
chr1    158534110
chr2    136231102
chr3    121005158
chr4    120000601
chr5    120089316
chr6    117806340
chr7    110682743
chr8    113319770
chr9    105454467
chr10   103308737
chr11   106982474
chr12   87216183
chr13   83472345
chr14   82403003
chr15   85007780
chr16   81013979
chr17   73167244
chr18   65820629
chr19   63449741
chr20   71974595
chr21   69862954
chr22   60773035
chr23   52498615
chr24   62317253
chr25   42350435
chr26   51992305
chr27   45612108
chr28   45940150
chr29   51098607
chrX    139009144
"""
# Parse list of chromosomes into a list of Chromosome objects which contain the
# chromosome name, length, mutation rate, and recombination rate
_chromosomes = []

for line in _chromosome_data.splitlines():
    name, length = line.split()[:2]
    _chromosomes.append(stdpopsim.Chromosome(
        id=name, length=int(length),
        mutation_rate=1e-8,
        recombination_rate=1e-8))

# A citation for the chromosome parameters. Additional citations may be needed if
# the mutation or recombination rates come from other sources. In that case create
# additional citations with the appropriate reasons specified (see API documentation
# for stdpopsim.citations)

_assembly_citation = stdpopsim.Citation(
    doi="https://doi.org/10.1093/gigascience/giaa021",
    year="2020",
    author="Rosen et al.",
    reasons={stdpopsim.CiteReason.ASSEMBLY})

# Create a genome object

_genome = stdpopsim.Genome(
    chromosomes=_chromosomes,
    assembly_citations=[_assembly_citation])

# Create a Species Object
_gen_time_citation = stdpopsim.Citation(
    doi="https://doi.org/10.1093/molbev/mst125",
    year="2013",
    author="MacLeod et al.",
    reasons={stdpopsim.CiteReason.GEN_TIME})

_pop_size_citation = stdpopsim.Citation(
    doi="https://doi.org/10.1093/molbev/mst125",
    year="2013",
    author="MacLeod et al.",
    reasons={stdpopsim.CiteReason.POP_SIZE})

_species = stdpopsim.Species(
    id="BosTau",
    name="Bos Taurus",
    common_name="Cattle",
    genome=_genome,
    generation_time=5,
    generation_time_citations=[_gen_time_citation],
    population_size=62000,
    population_size_citations=[_pop_size_citation]
)

stdpopsim.register_species(_species)


###########################################################
#
# Demographic models
#
###########################################################

def _inferred_1_M_13():
    id = "IonaInferredDemography"
    description = "Iona MacLeod's Inferred Demographic Model for Bos Taurus"
    long_description = """
    The Runs of Homozygosity-based infer of Demography from MacLeod et al. 2013.
    """
    populations = [
        stdpopsim.Population(id="FILL ME", description="FILL ME"),
    ]
    citations = [
        stdpopsim.Citation(
            author="MacLeod et al.",
            year="2013",
            doi="https://doi.org/10.1093/molbev/mst125",
            reasons={stdpopsim.CiteReason.DEM_MODEL})
    ]

    generation_time = 5

    # parameter value definitions based on published values

    return stdpopsim.DemographicModel(
        id=id,
        description=description,
        long_description=long_description,
        populations=populations,
        citations=citations,
        generation_time=generation_time,
        population_configurations=[
            msprime.PopulationConfiguration(
                initial_size=90, growth_rate=0.0166,
                metadata=populations[0].asdict())
        ],
        #migration_matrix=[
         #   "FILL ME"
        #],
        demographic_events=[
            msprime.PopulationParametersChange(
                # Here 'time' should be in generation notation, so if it is given in years, it should be replaced by T_0, T_1, ... , T_n; as shown above)
                # Growth rate is "per generation exponential growth rate": -alpha= [ln(initial_pop_size/next_stage_pop_size)/generation_span_in_years]
                # For example: ln(90/120)/3= -0.095894024
                time=1, initial_size=90, growth_rate=-0.095894024, population_id=0),
            msprime.PopulationParametersChange(
                time=4, growth_rate=-0.24465639, population_id=0),
            msprime.PopulationParametersChange(
                time=7, growth_rate=-0.0560787, population_id=0),
            msprime.PopulationParametersChange(
                time=13, growth_rate=-0.1749704, population_id=0),
            msprime.PopulationParametersChange(
                time=19, growth_rate=-0.0675775, population_id=0),
            msprime.PopulationParametersChange(
                time=25, growth_rate=-0.0022129, population_id=0),
            msprime.PopulationParametersChange(
                time=155, growth_rate=-0.0007438, population_id=0),
            msprime.PopulationParametersChange(
                time=455, growth_rate=-0.0016824, population_id=0),
            msprime.PopulationParametersChange(
                time=655, growth_rate=-0.0006301, population_id=0),
            msprime.PopulationParametersChange(
                time=1755, growth_rate=-0.0005945, population_id=0),
            msprime.PopulationParametersChange(
                time=2355, growth_rate=-0.0005306, population_id=0),
            msprime.PopulationParametersChange(
                time=3355, growth_rate=-0.0000434, population_id=0),
            msprime.PopulationParametersChange(
                time=33155, growth_rate=-0.0000, population_id=0),
            msprime.PopulationParametersChange(
                time=933155, growth_rate=-0.0, population_id=0),

        ],
    )


_species.add_demographic_model(_inferred_1_M_13())
