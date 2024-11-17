# Lit review

My first implementation of a web app that allows users to save reviews of journal articles. 

Hi! My name is Anand and I'm an R&D Engineer at HP Inc. Having been through grad school (PhD - Mechanical Engineering), I am familiar with the nitty gritty details of academic research. In most domains, it takes 6 months to a year for a research article to be published after submission given the relatively slow peer-review proces. While non peer-reviewed sources such as ArXiv are gaining popularity, it is hard to evaluate the quality of a research article. Scientific research would be significantly accelerated if we get peer-review results quickly. Moreover, the reviews are often not visible to the general public which makes it harder to get a feel for what the community thinks of the work. The only way to assess the impact of a paper is citations which is slow because of the time taken to publish.

My objective is two-fold:
1. Reduce the time to have a peer-reviewed published journal by more than an order of magnitude (from few months to few days).
2. Provide visibility to what the scientific community thinks of a particular work by making public the reviews of subject matter experts in the field.

This helps reduce the cycle time between initial results and further refinements. Moreover, the quick feedback of the community would help researchers fine tune their work in real time. To do this, one needs a platform where a decent fraction (at least over 30%; preferably over 50%) of a particular research community is present and active. Establishing such a community is a classic chicken-egg problem. Any individual researcher would be active only if their community of interest is active but the community is essentially a group of individual researchers. To tackle this problem, picking a right research community is essential. A good research community for this purpose should have the following traits:

1. Be small (so it is easy to convince over 30% to use the platform initially)
2. Have a larger fraction of early adopters (say someone in computational sciences?)

Such platforms exist for local fields (for instance Twitter/X or Reddit for Computer Science grads) but haven't penetrated into other fields. The reason could very well be lack of incentive for platform owners to push this platform to other areas. So in addition to solving this problem for one field, the platform should be applicable to most if not all fields.

Coming back to the chicken-egg problem, in order to solve this, one approach is to tackle a slightly different but related problem - Literature Review. Most graudate students, Professors and various researchers in national labs as well as industry do literature review on a routine basis to keep up with the state of the art in their fields. However, this review is scattered in word documents, power point slides, hand written notes, etc., As a firt part of this work, I'm building a website where users can save the reviews of articles they read. Once a sufficient number of people start using this platform, the next step would be to allow people to add their review of other people's work with room for replies. 

To get the v1 of this app going, here are the basic things that are necessary:

- [] login (this could be something simple like Andrej Karpathy's [ArXiv-Sanity](https://arxiv-sanity-lite.com/))
- [] home page that lists all papers reviewed
- [] ability to add reviews
- [] ability to edit/delete reviews
