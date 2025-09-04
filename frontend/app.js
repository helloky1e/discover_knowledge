const Home = {
  data() {
    return { profile: null };
  },
  mounted() {
    axios.get("/api/profile/").then((res) => {
      this.profile = res.data;
    });
  },
  template: `
    <div v-if="profile">
      <h1>{{ profile.name }}</h1>
      <p>{{ profile.introduction }}</p>
      <p>Contact: {{ profile.contact }}</p>
      <h3>Work Experience</h3>
      <p>{{ profile.work_experience }}</p>
    </div>
  `,
};

const Blog = {
  data() {
    return { posts: [] };
  },
  mounted() {
    axios.get("/api/blog/").then((res) => {
      this.posts = res.data.posts;
    });
  },
  template: `
    <div>
      <h1>Blog</h1>
      <div v-for="post in posts" :key="post.id" class="post">
        <h3>{{ post.title }}</h3>
        <p>{{ post.body }}</p>
      </div>
    </div>
  `,
};

const routes = [
  { path: "/", component: Home },
  { path: "/blog", component: Blog },
];

const router = VueRouter.createRouter({
  history: VueRouter.createWebHashHistory(),
  routes,
});

const app = Vue.createApp({});
app.use(router);
app.mount("#app");
