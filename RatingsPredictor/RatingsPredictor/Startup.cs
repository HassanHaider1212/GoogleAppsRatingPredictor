using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(RatingsPredictor.Startup))]
namespace RatingsPredictor
{
    public partial class Startup
    {
        public void Configuration(IAppBuilder app)
        {
            ConfigureAuth(app);
        }
    }
}
